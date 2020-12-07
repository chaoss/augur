import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DashboardComponent } from 'src/app/dashboard/dashboard.component';
import { LineGraphComponent } from './line-graph/line-graph.component';
import { GroupComponent } from 'src/app/group/group.component';

const routes: Routes = [
  {
    path: "",
    component: DashboardComponent,
  },
  {
    path: "graph",
    component: LineGraphComponent,
  },
  {
    path: "group/:rgId",
    component: GroupComponent,
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { 
}
