import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule } from '@angular/http';
import { FormsModule } from '@angular/forms';

import { AppComponent }  from './app.component';
import { PokemonComponent } from './pokemon.component';
import { PokemonService } from './pokemon.service';
import { AppRoutingModule } from './app-routing.module';
import { PokemonDetailComponent } from './pokemon-details.component';

@NgModule({
  imports:      [ BrowserModule, HttpModule, FormsModule, AppRoutingModule ],
  declarations: [ AppComponent, PokemonComponent, PokemonDetailComponent ],
  providers: [ PokemonService ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
