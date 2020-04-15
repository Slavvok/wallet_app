import { Injectable } from '@angular/core';
import { HttpClientModule, HttpClient, HttpHeaders } from '@angular/common/http';
import { UserService } from './user.service';
import { environment } from 'src/environments/environment';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class WalletAppService {
  private url = environment.apiUrl;

  constructor(private http: HttpClient) { }

  getOneWallet(id) {
    return this.http.get<any>(this.url + `/wallets/${id}/`, httpOptions)
  }

  getWallets() {
    return this.http.get<any>(this.url + '/wallets/', httpOptions)
  }

  getWalletTransactions(id) {
    return this.http.get<any>(this.url + `/wallets/${id}/transactions/`, httpOptions)
  }

  createWallet(new_wallet) {
    return this.http.post<any>(this.url + '/wallets/', new_wallet, httpOptions)
  }

  removeWallet(id) {
    return this.http.delete<any>(this.url + `/wallets/${id}/`, httpOptions)
  }

  getTransactions() {
    return this.http.get<any>(this.url + '/transactions/', httpOptions)
  }

  createAddTransaction(transaction) {
    return this.http.post<any>(this.url + '/add-transaction/', transaction, httpOptions)
  }

  createSubTransaction(transaction) {
    return this.http.post<any>(this.url + '/sub-transaction/', transaction, httpOptions)
  }
}
