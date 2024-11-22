import { Observable } from "rxjs"
import QueryParams from "../../models/queryParams.model"
import api from "../api-config/rxjs";
import Account from "../../models/account.model";

export class AccountRest{
    getAll(query:QueryParams): Observable<any> {
        const url :string = `/accounts`
        return api.get(url,query)
    }
    getById(id:number): Observable<any>{
        const url: string = `/accounts/${id}`
        return api.get(url)
    }
    delete(id:number): Observable<any>{
        const url: string = `/accounts/delete/${id}`
        return api.deleteR(url)
    }
    register(account: Account): Observable<any>{
        const url:string = `/accounts/create`
        return api.post(url, account)
    }
    update(account: Account,id:number): Observable<any>{
        const url:string = `/accounts/update/${id}`
        return api.put(url,account)
    }
    updateStatus(id:number, status:string): Observable<any>{
        const url: string = `/accounts/updateStatus/${id}`
        return api.patch(url,{status:status})
    }

    
}