Wallet_app written with Django REST Framework and Angular.

Authentication: 
```
   POST /auth-token-auth {*"username": str, *"password": str} - get <token>
```
App: ( Headers: {"Authentication": "JWT <token>"} )
```
   GET /wallets POST /wallets {*"name": str}
   GET /wallets/<id>/transactions
   GET /transactions
   POST /add-transactions {*"value": int, *"wallet_id": int, "commentary": str}
   POST /sub-transactions {*"value": int, *"wallet_id": int, "commentary": str}
```

Initial start:

Create .env file, add variables 
```
     DATABASE_NAME=
     DATABASE_USER=
     DATABASE_PASSWORD=
     DATABASE_HOST=
     DATABASE_PORT=
```
Change apiUrl to your external ip port in
```
wapp-frontend/src/environments/environment.prod.ts
```
Run
```
sudo docker-compose up -d --build
```

