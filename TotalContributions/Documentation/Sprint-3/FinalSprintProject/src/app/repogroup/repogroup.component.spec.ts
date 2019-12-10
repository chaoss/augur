import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RepogroupComponent } from './repogroup.component';

describe('RepogroupComponent', () => {
  let component: RepogroupComponent;
  let fixture: ComponentFixture<RepogroupComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RepogroupComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RepogroupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
