import { Routes, RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';

import { PokemonComponent } from './pokemon.component';
import { PokemonDetailComponent } from './pokemon-details.component';

const routes: Routes = [
  { path: 'home', component: PokemonComponent },
  { path: 'details/:id', component: PokemonDetailComponent },
  { path: '', redirectTo: '/home', pathMatch: 'full' }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})

export class AppRoutingModule { }
