import { TestBed } from '@angular/core/testing';

import { RepoInfoService } from './repo-info.service';

describe('RepoInfoService', () => {
  let service: RepoInfoService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RepoInfoService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
