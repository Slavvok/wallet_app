import { Component, OnInit } from '@angular/core';
import { WalletAppService } from '../wallet-app.service'
@Component({
  selector: 'app-transactions',
  templateUrl: './transactions.component.html',
  styleUrls: ['./transactions.component.css']
})
export class TransactionsComponent implements OnInit {
  transactions: any;

  constructor(
    private walletService: WalletAppService
  ) { }

  ngOnInit(): void {
    this.getTransactions();
  }

  getTransactions() {
    this.walletService.getTransactions().subscribe(
      data => (this.transactions = data)
    )
  }
}
