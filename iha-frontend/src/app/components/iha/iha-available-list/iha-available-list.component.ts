import { Component, OnInit } from '@angular/core';
import {IhaDto} from "../../../models/IhaDto";
import {IhaService} from "../../../services/iha.service";
import {FormBuilder, FormGroup} from "@angular/forms";

@Component({
  selector: 'app-iha-available-list',
  templateUrl: './iha-available-list.component.html',
  styleUrls: ['./iha-available-list.component.css']
})
export class IhaAvailableListComponent implements OnInit {
  availableIhaList: IhaDto[] = []
  ihaCreateForm!: FormGroup
  ihaUpdateForm!: FormGroup
  constructor(private formBuilder: FormBuilder, private ihaService: IhaService) {
    this.ihaCreateForm = this.formBuilder.group({
      marka: [],
      model: [],
      agirlik: [],
      kategori: []
    })
    this.ihaUpdateForm= this.formBuilder.group({
      id: [],
      marka: [],
      model: [],
      agirlik: [],
      kategori: []
    })
  }

  ngOnInit(): void {
    this.fetch()
  }

  fetch() {
    this.ihaService.read().subscribe(data => {
      this.availableIhaList = data
    })
  }

  createIha() {
    this.ihaService.postIha(this.ihaCreateForm.value).subscribe(data => {
      this.fetch()
    })
  }


  updateIha(iha: any, propertyKey: string) {
    const updatedValue = (event?.target as HTMLTableCellElement).innerText;
    iha[propertyKey] = updatedValue;
    this.ihaService.updateIha(iha).subscribe(data => {
      this.fetch()
    })
  }
  deleteIha(iha: IhaDto){
    this.ihaService.deleteIha(iha).subscribe(data => {
      this.fetch()
    })
  }
}
