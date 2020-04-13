import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { UserService } from './user.service';
import { JwtInterceptor } from './login/jwt.interceptor';
import { WalletsComponent } from './wallets/wallets.component';
import { TransactionsComponent } from './transactions/transactions.component';
import { OneWalletComponent } from './one-wallet/one-wallet.component';
import { CreateTransactionComponent } from './create-transaction/create-transaction.component'

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    WalletsComponent,
    TransactionsComponent,
    OneWalletComponent,
    CreateTransactionComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    // NgbModule
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: JwtInterceptor, multi: true}
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
