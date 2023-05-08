import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-crud',
  templateUrl: './crud.component.html',
  styleUrls: ['./crud.component.scss']
})
export class CrudComponent {
  StudentArray : any[] = [];

  name: string =""; 
  address: string ="";
  fee: Number =0;

  currentStudentID = "";

  constructor(private http: HttpClient )
  {
    //this.getAllStudent();
  }

  saveRecords()
  {
  
    let bodyData = {
      "name" : this.name,
      "address" : this.address,
      "fee" : this.fee
    };
    this.http.post("http://127.0.0.1:8000/student",bodyData).subscribe((resultData: any)=>
    {
        console.log(resultData);
        alert("Student Registered Successfully");
        //this.getAllStudent();
    });
  }
}
