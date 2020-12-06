import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { RepoListComponent } from './repo-list/repo-list.component';

const routes: Routes = [
  {path: 'repos', component: RepoListComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
