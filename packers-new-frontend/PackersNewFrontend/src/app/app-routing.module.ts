import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DashboardComponent } from 'src/app/dashboard/dashboard.component';
import { LineGraphComponent } from './line-graph/line-graph.component';
import { GroupComponent } from 'src/app/group/group.component';
import { RepoComponent } from 'src/app/repo/repo.component';

const routes: Routes = [
  {
    path: "",
    component: DashboardComponent,
  },
  {
    path: "group/:rgId",
    component: GroupComponent,
  },
  {
    path: "repoInfo/:repoId",
    component: RepoComponent,
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { 
}
