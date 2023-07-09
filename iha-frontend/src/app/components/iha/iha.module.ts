import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { IhaAvailableListComponent } from './iha-available-list/iha-available-list.component';
import { IhaRentedListComponent } from './iha-rented-list/iha-rented-list.component';
import {AppRoutingModule} from "../../app-routing.module";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";



@NgModule({
  declarations: [
    IhaAvailableListComponent,
    IhaRentedListComponent
  ],
    imports: [
        CommonModule,
        AppRoutingModule,
        ReactiveFormsModule,
        FormsModule
    ]
})
export class IhaModule { }
