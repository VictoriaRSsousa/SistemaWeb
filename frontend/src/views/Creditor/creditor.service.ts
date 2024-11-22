import Creditor from "../../models/creditor.model";
import QueryParams from "../../models/queryParams.model";
import { CreditorRest } from "../../services/rest/creditor.rest";
import { Observable, Subject, take} from "rxjs";

export class CreditorService {
  constructor(private _CreditorRest: CreditorRest = new CreditorRest()) {}

  private creditor$: Subject<any> = new Subject<any>();
  private creditors$: Subject<any> = new Subject<any>();

  

  creditor: Observable<any> = this.creditor$.asObservable();
  creditors: Observable<any> = this.creditors$.asObservable();


    getAll(query:QueryParams): void{
        this._CreditorRest.getAll(query).pipe().subscribe({
            next:(response)=>{
                this.creditors$.next(response)
                
            }
        })
    }
    getByCnpj(cnpj: string):void{
        this._CreditorRest.getBycnpj(cnpj).pipe(take(1)).subscribe({
            next:(response)=>{
                this.creditor$.next(response)
            }
        })
    }
    delete(cnpj:string): void {
        this._CreditorRest.delete(cnpj).pipe(take(1)).subscribe({
            next:(response)=>{
                this.creditor$.next(response)
            }
        })
    }
    register(creditor:Creditor){
        this._CreditorRest.register(creditor).pipe(take(1)).subscribe({
            next:(response)=>{
                this.creditor$.next(response)
            }
        })
    }
    update(creditor:Creditor, cnpj:string){
        this._CreditorRest.update(creditor,cnpj).pipe(take(1)).subscribe({
            next:(response)=>{
                this.creditor$.next(response)
            }
        })
    }
    


}