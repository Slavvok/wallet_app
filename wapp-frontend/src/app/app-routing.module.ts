import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AuthGuard } from './login/auth.guard';
import { LoginComponent } from './login/login.component';
import { WalletsComponent } from './wallets/wallets.component';
import { OneWalletComponent } from './one-wallet/one-wallet.component'
import { TransactionsComponent } from './transactions/transactions.component';
import { CreateTransactionComponent } from './create-transaction/create-transaction.component';

const routes: Routes = [
  {path: 'login', component: LoginComponent},
  {path: 'wallets', component: WalletsComponent, canActivate: [AuthGuard]},
  {path: 'wallets/:id', component: OneWalletComponent, canActivate: [AuthGuard],
    children: [
      {path: 'add-transaction', component: CreateTransactionComponent, },
      {path: 'sub-transaction', component: CreateTransactionComponent, }
    ]},
  {path: 'transactions', component: TransactionsComponent, canActivate: [AuthGuard]}
];

@NgModule({
  imports: [RouterModule.forRoot(routes,
    {
      enableTracing: false
    }
  )],
  exports: [RouterModule]
})
export class AppRoutingModule { }
