import type { Observable } from 'rxjs'
import api from "../api-config/rxjs";
import QueryParams from '../../models/queryParams.model';
import Creditor from '../../models/creditor.model';
export class CreditorRest {



    getAll(query:QueryParams): Observable<any> {
        const url :string = `/creditors`
        return api.get(url,query)
    }
    getBycnpj(cnpj:string): Observable<any>{
        const url: string = `/creditors/${cnpj}`
        return api.get(url)
    }
    delete(cnpj:string): Observable<any>{
        const url: string = `/creditors/delete/${cnpj}`
        return api.deleteR(url)
    }
    register(creditor: Creditor): Observable<any>{
        const url:string = `/creditors/create`
        return api.post(url, creditor)
    }
    update(creditor:Creditor,cnpj:string): Observable<any>{
        const url:string = `/creditors/update/${cnpj}`
        return api.put(url,creditor)
    }

}