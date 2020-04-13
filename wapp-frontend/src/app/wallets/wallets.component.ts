import { Component, OnInit, Input } from '@angular/core';
import { UserService } from '../user.service';
import { WalletAppService } from '../wallet-app.service';

@Component({
  selector: 'app-wallets',
  templateUrl: './wallets.component.html',
  styleUrls: ['./wallets.component.css']
})
export class WalletsComponent implements OnInit {

  @Input() new_wallet = {name: ''}

  wallets: any;
  isRemove: boolean;
  isCreate: boolean;
  removeId: number;

  constructor(
    private userService: UserService,
    private walletService: WalletAppService,
  ) { }

  ngOnInit(): void {
    this.getWallets();
  }

  getWallets() {
    this.walletService.getWallets().subscribe(
      data => (this.wallets = data)
    )
  }

  createWallet() {
    this.walletService.createWallet(this.new_wallet).subscribe(
      data => (console.log(data))
    )
  }

  removeWallet() {
    this.walletService.removeWallet(this.removeId).subscribe(
      data => {
        console.log(data);
        this.closeModal();
      }
    )
  }

  openModal(id) {
    this.isRemove = true;
    this.removeId = id;
    console.log(this.isRemove);
  }

  closeModal() {
    this.isRemove = false;
    this.removeId = null;
  }

  createModal() {
    this.isCreate = !this.isCreate;
  }
}
