import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DashboardComponent } from 'src/app/dashboard/dashboard.component';
import { LineGraphComponent } from './line-graph/line-graph.component';

const routes: Routes = [
  {
    path: "",
    component: DashboardComponent,
  },
  {
    path: "graph",
    component: LineGraphComponent,
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { 
}
