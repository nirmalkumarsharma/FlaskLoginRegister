import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'
import { AuthenticationService, TokenPayload } from '../authentication.service'

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  constructor(private auth: AuthenticationService, private router: Router) { }

  ngOnInit() {
  }


  credentials: TokenPayload=
  {
    id:0,
    first_name:'',
    last_name:'',
    email:'',
    password:''
  }

  register()
  {
    this.auth.register(this.credentials).subscribe(
      ()=>{
        this.router.navigateByUrl('/login')
      },
      err=>{
        console.error(err)
      }
    )
  }
}
