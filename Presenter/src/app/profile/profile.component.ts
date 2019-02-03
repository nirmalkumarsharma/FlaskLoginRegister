import { Component, OnInit } from '@angular/core';
import { AuthenticationService, UserDetails } from '../authentication.service'

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  details: UserDetails

  constructor(private auth: AuthenticationService) { }

  ngOnInit()
  {
    this.details=this.auth.getUserDetails()
  }
}
