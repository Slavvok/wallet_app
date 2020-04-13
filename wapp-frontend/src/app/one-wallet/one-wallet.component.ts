import { Component, OnInit, Input } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { WalletAppService } from '../wallet-app.service'

@Component({
  selector: 'app-one-wallet',
  templateUrl: './one-wallet.component.html',
  styleUrls: ['./one-wallet.component.css']
})
export class OneWalletComponent implements OnInit {
  _id: number;
  isAdd: boolean = false;
  isSub: boolean = false;
  isDetail: boolean;
  wallet: any;

  @Input() transaction = {
    value: 0,
    commentary: '',
    wallet_id: null,
  }

  constructor(
    private router: ActivatedRoute,
    private walletService: WalletAppService,
  ) { }

  ngOnInit(): void {
    this._currentId();
    this.wallet = this.walletService.getWalletTransactions(this._id).subscribe(
      data => (this.wallet = data)
    );
  }

  _currentId() {
    this.router.url.subscribe(
      data => {this._id = +data[1].path; });
    this.transaction.wallet_id = this._id;
  }

  createTransaction() {
    console.log(this.transaction);
    if (this.isAdd) {
    this.walletService.createAddTransaction(this.transaction).subscribe(
      data => {console.log(data);
        this.wallet.value = data.post_trans_value;
      }
    )} else {
    this.walletService.createSubTransaction(this.transaction).subscribe(
      data => {console.log(data);
        this.wallet.value = data.post_trans_value;
      }
    )}
  }

}
