import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CommitsOverTimeComponent } from './commits-over-time.component';

describe('CommitsOverTimeComponent', () => {
  let component: CommitsOverTimeComponent;
  let fixture: ComponentFixture<CommitsOverTimeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CommitsOverTimeComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CommitsOverTimeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
