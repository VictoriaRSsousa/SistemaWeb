export default class QueryParams {
    constructor(
      public cnpj?: string ,
      public email?: string ,
      public status?: string,
      public data_pagamento?: Date,
      public data_vencimento?: Date,
    ) {}
  }
  