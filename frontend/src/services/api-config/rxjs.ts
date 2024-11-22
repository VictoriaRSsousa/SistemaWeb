import type { ResponseType } from "axios";
import { Observable, defer, map } from "rxjs";
import { api } from "./config";

const get = <T>(
    url: string,
    params?: object,
    baseURL?: string,
    responseType: ResponseType = "json",
    token?: any
  ): Observable<T> => {
    return defer(() =>
      api(baseURL, token).get<T>(url, { params, responseType })
    ).pipe(map((result) => result.data));
  };
  
  const post = <T>(
    url: string,
    body: object,
    params?: object,
    baseURL?: string
  ): Observable<T | void> => {
    return defer(() => api(baseURL).post<T>(url, body, { params })).pipe(
      map((result) => result.data)
    );
  };
  
  const put = <T>(
    url: string,
    body: object,
    params?: object,
    baseURL?: string
  ): Observable<T | void> => {
    return defer(() => api(baseURL).put<T>(url, body, { params })).pipe(
      map((result) => result.data)
    );
  };
  
  const patch = <T>(
    url: string,
    body: object,
    params?: object,
    baseURL?: string
  ): Observable<T | void> => {
    return defer(() => api(baseURL).patch<T>(url, body, { params })).pipe(
      map((result) => result.data)
    );
  };
  
  const deleteR = <T>(url: string, baseURL?: string): Observable<T | void> => {
    return defer(() => api(baseURL).delete(`${url}`)).pipe(
      map((result) => result.data)
    );
  };

  export default { get, post, put, patch, deleteR };