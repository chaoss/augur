import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {HomeComponent} from'../app/home/home.component';
import {ReposComponent} from'../app/repos/repos.component';
import {AnalysisComponent} from'../app/analysis/analysis.component';


const routes: Routes = [
  {
    path:"",
    redirectTo: 'home',
    pathMatch: 'full'
  },
  {
    path: 'home',
    component: HomeComponent,
   },
   {
    path: 'repos',
    component: ReposComponent,
   },
   {
    path: 'analytics',
    component: AnalysisComponent,
   },
  
    
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
