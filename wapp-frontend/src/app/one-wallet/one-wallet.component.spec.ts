import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { OneWalletComponent } from './one-wallet.component';

describe('OneWalletComponent', () => {
  let component: OneWalletComponent;
  let fixture: ComponentFixture<OneWalletComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ OneWalletComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(OneWalletComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
