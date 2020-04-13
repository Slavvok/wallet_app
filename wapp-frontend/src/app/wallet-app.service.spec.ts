import { TestBed } from '@angular/core/testing';

import { WalletAppService } from './wallet-app.service';

describe('WalletAppService', () => {
  let service: WalletAppService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(WalletAppService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
