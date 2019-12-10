import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { RepoComponent } from './repo/repo.component'
import { RepogroupComponent } from './repogroup/repogroup.component';
import { HomeComponent } from './home/home.component'
import { InfoComponent } from './info/info.component';
import { ContributorsComponent } from './contributors/contributors.component'
import { MessagesComponent } from './messages/messages.component';

const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'repogroup', component: RepogroupComponent },
  { path: 'repo', component: RepoComponent },
  { path: 'home', component: HomeComponent },
  { path: 'info/:groupId/:repoId', component: InfoComponent },
  { path: 'contributors/:groupId', component:ContributorsComponent },
  { path: 'messages/:groupId', component:MessagesComponent},
  { path: '**', redirectTo: '/home', pathMatch: 'full' }
  ];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
export const routingComponents = [HomeComponent,RepogroupComponent, InfoComponent, RepoComponent,ContributorsComponent,MessagesComponent ]
