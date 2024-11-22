import Creditor from "./creditor.model";

export default class Account {
  constructor(
    public data_pagamento:  string | undefined,
    public cnpj: string = '',
    public data_vencimento:  string='',
    public descricao: string='',
    public id: number=0,
    public status: string='',
    public valor: number=0,
    public multa: number=0,
    public juros: number=0,
    public credor: Creditor = new Creditor()
  ) {}
}
