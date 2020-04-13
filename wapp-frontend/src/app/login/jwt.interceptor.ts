import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpErrorResponse
} from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, take, switchMap } from 'rxjs/operators';

import { UserService } from '../user.service';

@Injectable()
export class JwtInterceptor implements HttpInterceptor {

  private isRefreshing = false;

  constructor(private userService: UserService) {}

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<any>> {
    var currentUser = this.userService.currentUserValue;
    if (currentUser && currentUser.token) {
      request = this.addToken(request, currentUser.token);
    }

    return next.handle(request).pipe(catchError(err => {
            if (err.status === 401) {
                // auto logout if 401 response returned from api
                this.userService.logout();
                location.reload(true);
            }

            const error = err.error.message || err.statusText;
            return throwError(error);
        }))
  }

  private addToken(request: HttpRequest<any>, token: string) {
    return request.clone({
      setHeaders: {
        Authorization: `JWT ${token}`
      }
    })
  }

}
