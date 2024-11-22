import QueryParams from "../../models/queryParams.model";
import { Observable, Subject, take} from "rxjs";
import Account from "../../models/account.model";
import { AccountRest } from "../../services/rest/account.service";

export class AccountService {
  constructor(private _AccountRest: AccountRest = new AccountRest()) {}

  private account$: Subject<any> = new Subject<any>();
  private accounts$: Subject<any> = new Subject<any>();

  account: Observable<any> = this.account$.asObservable();
  accounts: Observable<any> =this.accounts$.asObservable();

    getAll(query:QueryParams): void{
        this._AccountRest.getAll(query).pipe().subscribe({
            next:(response)=>{
                this.accounts$.next(response)
                
            }
        })
    }
    getById(id: number):void{
        this._AccountRest.getById(id).pipe(take(1)).subscribe({
            next:(response)=>{
                this.account$.next(response)
            }
        })
    }
    delete(id:number): void {
        this._AccountRest.delete(id).pipe(take(1)).subscribe({
            next:(response)=>{
                this.account$.next(response)
            }
        })
    }
    register(account:Account){
        this._AccountRest.register(account).pipe(take(1)).subscribe({
            next:(response)=>{
                this.account$.next(response)
            }
        })
    }
    update(account:Account, id:number){
        this._AccountRest.update(account,id).pipe(take(1)).subscribe({
            next:(response)=>{
                this.account$.next(response)
            }
        })
    }
    updateStatus(id:number, status:string){
        this._AccountRest.updateStatus(id,status).pipe(take(1)).subscribe({
            next:(response)=>{
                this.account$.next(response)
            }
        })
    }


}