import { Component, OnInit, Input } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { first } from 'rxjs/operators';

import { UserService } from '../user.service';
import { User } from '../user';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  @Input() user: User = {
    username: '',
    password: ''
  }
  returnUrl: string;

  constructor(private userService: UserService,
              private location: Location,
              private router: Router,
              private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
  }

  login(): void {
    this.userService.loginUser(this.user)
    .pipe(first())
    .subscribe(
      resp => {
        this.router.navigate([this.returnUrl]);
      }
    )
  }

}
