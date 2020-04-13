import { Injectable } from '@angular/core';
import { HttpClientModule, HttpClient, HttpHeaders } from '@angular/common/http';
import { UserService } from './user.service';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class WalletAppService {
  constructor(private http: HttpClient,
              private userService: UserService,
  ) { }

  getOneWallet(id) {
    return this.http.get<any>(this.userService.userUrl + `/wallets/${id}/`, httpOptions)
  }

  getWallets() {
    return this.http.get<any>(this.userService.userUrl + '/wallets', httpOptions)
  }

  getWalletTransactions(id) {
    return this.http.get<any>(this.userService.userUrl + `/wallets/${id}/transactions`, httpOptions)
  }

  createWallet(new_wallet) {
    return this.http.post<any>(this.userService.userUrl + '/wallets/', new_wallet, httpOptions)
  }

  removeWallet(id) {
    return this.http.delete<any>(this.userService.userUrl + `/wallets/${id}/`, httpOptions)
  }

  getTransactions() {
    return this.http.get<any>(this.userService.userUrl + '/transactions-list', httpOptions)
  }

  createAddTransaction(transaction) {
    return this.http.post<any>(this.userService.userUrl + '/add-transaction/', transaction, httpOptions)
  }

  createSubTransaction(transaction) {
    return this.http.post<any>(this.userService.userUrl + '/sub-transaction/', transaction, httpOptions)
  }
}
