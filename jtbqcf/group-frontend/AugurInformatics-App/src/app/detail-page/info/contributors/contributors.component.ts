import { Component, OnInit, Input } from '@angular/core';
import { DataService } from '../../../data.service';

@Component({
  selector: 'app-contributors',
  templateUrl: './contributors.component.html',
  styleUrls: ['./contributors.component.css']
})
export class ContributorsComponent implements OnInit {

  contributors: any;

  //@Input grabs the variable sent from the parent component. This can now just be used as normal
  @Input() urlGroupId: string;
  @Input() urlRepoId: string;

  constructor(private dataService: DataService) { }

  ngOnInit() {
    
    //calling function in data service that reads the endpoint. It is then assigned to the contributors object varibable 
    //declared above
    this.dataService.getInfo(this.urlGroupId, this.urlRepoId, 'contributors').subscribe(data => {
      this.contributors = data;
  
    }
    );
  }

}
