import type { AxiosError, AxiosInstance, AxiosRequestConfig } from "axios";
import axios from "axios";
import { Toasts } from "../../utils/toasts.util";

function apiConfig(baseUrl: string): AxiosRequestConfig {
    return {
        baseURL: baseUrl,
    }
}

function initAxios(config: AxiosRequestConfig, token?: any): AxiosInstance {
    const showToast = new Toasts()
    const defineInstance = axios.create(config);
    defineInstance.interceptors.request.use((config) => {
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    }, (error) => {
        showToast.showError(error?.name,error?.message)
        return Promise.reject(error);
    });

    defineInstance.interceptors.response.use((response) => {
        return response;
    }, (error: AxiosError) => {
        showToast.showError(error?.name,error?.message)
        
        return Promise.reject(error);
    });

    return defineInstance;
}

function api(baseURL: string = "/api", token?: any): AxiosInstance {
    return initAxios(apiConfig(baseURL), token);
}

export { api }