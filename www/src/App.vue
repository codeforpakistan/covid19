<template>
  <div id="app" class="container-fluid py-3">
    <div class="d-flex align-items-center">
      <img src="https://upload.wikimedia.org/wikipedia/commons/e/ef/State_emblem_of_Pakistan.svg" height="80" class="mr-3 d-none d-md-block">
      <div class="flex-grow-1">
    <small>Ministry of National Health Services Regulation and Coordination, Government of Pakistan.</small>
        <h1 class="text-secondary">COVID-19 PAKISTAN DASHBOARD</h1>
      </div>
      <span>Last Updated: <strong>{{ today }} 1:00pm</strong></span>
    </div>
    <hr>

    <!-- FIRST ROW -->
    <div class="row">
      <div class="col-6 col-md-3">
        <div class="card card-body border-0 shadow-sm mb-4">
          <h3 class="card-title text-primary low display-4 font-weight-normal">{{ admitted + discharged + expired }}</h3>
          <p class="card-text">CONFIRMED</p>
        </div>
      </div>
      <div class="col-6 col-md-3">
        <div class="card card-body border-0 shadow-sm mb-4">
          <h3 class="card-title text-warning low display-4 font-weight-normal">{{ admitted }}</h3>
          <p class="card-text">ADMITTED</p>
        </div>
      </div>
      <div class="col-6 col-md-3">
        <div class="card card-body border-0 shadow-sm mb-4">
          <h3 class="card-title text-success low display-4 font-weight-normal">{{ discharged }}</h3>
          <p class="card-text">DISCHARGED</p>
        </div>
      </div>
      <div class="col-6 col-md-3">
        <div class="card card-body border-0 shadow-sm mb-4">
          <h3 class="card-title text-danger low display-4 font-weight-normal">{{ expired }}</h3>
          <p class="card-text">EXPIRED</p>
        </div>
      </div>
    </div>
    <!--END FIRST ROW-->

    <!-- SECOND ROW -->
    <div class="row mb-4">
      <div class="col-md-6">
        <svg version="1.1"
          id="svg82" inkscape:version="0.92.4 (5da689c313, 2019-01-14)" sodipodi:docname="PAK_AU_T1_v2.svg" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:svg="http://www.w3.org/2000/svg"
          xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 1000 800"
          style="enable-background:new 0 0 1000 800;" xml:space="preserve">

        <path id="Sindh" :fill="colorme('Sindh')" stroke="#f8f9fa" d="M520.9,742.9l-1.5-9.7l4.8-5.2l-7-13.2l-3.5-13.2l-10.5-14l0.3-15.8l-3-2.7l-10.1,2.1l-6.7-1.8
          l-3.3-4.8l-5.4-7.9l-1.1-7.2l4.6-10.8l-0.2-17.5l-5.1-2.8l-9.3,1l-19.5-10.5l1.1-14.4l3.7-9.4l11.9-12.3l10-10.3l4.2-11.3l4.9-6.7
          l-9-4.2l-6.5-8.9l-3.1-12.3l-5.8-8.4l-11.8-3.1l-4.8,2.2l-17.5,0.6l-28.2,1l-5.9,7.1l-16.3,10.7l-5.3,7.6l-13,5.7l-13.8,3l-7.9,16.8
          l-4.8,14.6l0.7,36.7l4,13.4l11.4,19.9l-0.3,14.8l-3.6,10.9l-10.4,13.6l-1.7,9.1l-5.3,5.4l-0.2,3.6l-4,4.7l-3.4,0.3l-8.5,7.3
          l-2.5,3.8l10.2-1.7l4.9,2.9l-0.1-2.1l6,4.3l0.1-1.8l5.3,2.5l2.5-1.2l1.1,2.1l-3,1.5l-2.5,4l0.5,2l2.8-0.2l2,1.6l-3,1.6l1.9,1.9
          l1.4,6.3l1.4-1.3l-0.4,4.5l4.1,0.9l-3.6,1.7l2.5,12.8l9.9,2l0.1,6.7l-1.9,3.7l5.7,1.6l1.6-4.7l1.5,7.8l3.3-0.2l-1.1-2.6l5.9,1.8
          l1-5.8l8.3,8.3l-0.7-9.8l2.8,1.2l1.7,6.3l-2.5,4.8l2.3,1.4l0.5-1.9l2.2,2.5l0.4-12.1l1.9,7.2l2.3-7.2l6.4-4.8l19,1.1l0.7-18.2
          l3.1-1.7l1.5,6.1l3.4-5.4l3.5,4.1l4.9-2.5l5.4,1.9l5.5-2.4l6.6,0.4l7.4-0.9l6.7,6.4l15,0.3l4.3-6.6l13-4l10.2-3.8l1,1.7l-1.6,1.9
          l0.6,6l5,1.7l6.6,0.1l4.9-2.5l-1.9-1.9l5.7-3.7l1.7,0.6l5.5-3.3L520.9,742.9z"/>
        <path id="Balochistan" :fill="colorme('Balochistan')" stroke="#f8f9fa" d="M481.6,361.1l-1.2-2.5l2-12.4l-0.7-8.5l-8.3,4l-2.8,4.9l-1.3-8.4l-4.3-2.6l1.2-21.9l-3.8,2.6
          l-1.5-1.6l1.9-4.1l-3.6-2.3l1.5-4.8l-8.4,2.3l-5.3,5.8l-10.9-0.5l-6.3,5.3l-3.9,8.4l-5,4.4l-3.6-1.1l-2.6,2.5l-4.6-0.5l-4.4-4.9
          l-0.7-4.3l-3.1-0.3l-3.5-3l-6.9,3.7l-7.3,0.4l-5.9-4.5l-5.2,7.8l-10,6l-7.5,4.6l-8-0.8l3,7.4l7.7-0.8l0.9,4l-21,8l-3.4-0.3
          l-12.1-1.1l-2-5.4l-14.3,6.4l-2.4,7.9l-6,5.6l-8.6,2.1l-5.5,21.4l3.7,8.5l-5.6,21.1l5.9,4.8l-5.3,6.6l-59.4,18.4l-21.7-2.6
          l-18.3,3.3l-8.1,8.5l-25.7-6.5l-56.7,5.8l-78.9-27.2L37.9,461l6.4,18.9L60.1,501l15.6,8.9l13.2,2.9l10.6,10.3l10-1.2l-1,14.9l4,26.9
          l-3.4,18.1l8,2.4l12-2.8l6.7,5.9l-3.1,3.2l1.3,12l-4.5,1.8l-1.1,11.3l-18.3-0.3l-26.5,7.5l1,9.9l-7.1-2.1l-1.4,3.8L62,639.6
          l-3.6,24.6l-4,0.2l1.4,7.3l-5.1,27l8.3,0.7l-2.3,8.5l5.4,0.5l0.8-3.1l12.4-1l-1.9-2.7l1.8-3l5.9-1l4.3,2.1l-1.2,4.8h5.3l-2.6-2.8
          l7.3-3.6l-0.9-1.5l13.5-1.2l13.5,2.6l5-2.2l20.1,3.5l0.7-1.2l-2.6-4.1l5-4.4l8.8-1.4l9.1,2.9l7.1-0.4l-1.8-4.2l-1.3,1.5l-1.6-1.6
          l3.1-2l5.7,0.2l-0.9,1.5l-2.7,1.2l2,4.3l6.7,0.7l8.9,4.8l5.4-2.3l4.5,3.6l-1.5,2l2.2,0.6l3-0.9l-2.3-2.3l1.2-3.7l5.2-2.3l14.7,0.8
          l4.3,0.9l3.5-4.6l2.9,0.5l2.6-1.5l2,1.6l3.4-1.1l10.6,2.2l9.5-4.3l22.2-2.9l9.5,4l0.9-0.4l-2.4-3l1.4-1.3l-2.1-0.7l-1.2,0.7
          l-4.2-4.1l-3.8,0.5l-2.5,3.1l-3.9-1l1.2-3.2l5.6-2.6l2.2,0.7l3.1-1.5l6.8,6.6l0.8-0.8l2.8,7.9l-1.7,0.2l1.2,2.7l7.8,7.8l-2.5,17.2
          l1.2,0.4l8.5-7.3l3.4-0.3l4-4.7l0.2-3.6l5.3-5.4l1.7-9.1l10.4-13.6l3.6-10.9l0.3-14.8L331.2,627l-4-13.4l-0.7-36.7l4.8-14.6
          l7.9-16.8l13.8-3l13-5.7l5.3-7.6l16.3-10.7l5.9-7.1l33.2-1.2l12.5-0.4l-2.5-6l5.6-3.2l4.3-10.1l-1.9-5.4l10.5-10.9l2.3-12l-2.7,1.5
          l-2.4-3.3l1.1-3.5l-5.3-1.7l2.1-13.4l6.7-2.7l7.8-11.4l4.1-11.9l3.8-7.6l-4.8,1.9l-1.8-3.5l2.1-8.7l5.3-10.4l-0.5-4.6l6-6.6l3.1-0.4
          l-1.1-3.1L481.6,361.1z"/>
        <path id="Punjab" :fill="colorme('Punjab')" stroke="#f8f9fa" d="M735.5,287.9l-6.2-4.6l-3,0.2l-3.9-4.1l-3.9,2.6l-3.7-1.4l-4-1.4l-6,0.6l-3.2-6.2l0.8-7.2l2.4-7
          l-8.3,5.7l-4.2-4.6l-6.4,0.2l-15.4-7.5l-4.5-5l-5.8,1.5l-8.8-4.9l1.6-3.6l-1.3-3.5l-3.3-8.9l3.1-8.9l-3.1-5.6l1.5-4.3l-4.3-18
          l-6.6,3l-2.3,4.7l-8.3,4.6l5.3,3.9l1.4-0.1l1.6,2.1l-3.9,3.9l-0.8,4.5l-5.6,3.6l-3-2.4l1.9-1.5l-3.4-5.1l-9,4.4l-3.2-6.9l5.9-1.8
          l-5.4-2.1l2.6-2.4l-1.3-4.5l-4.3-2.9l-3.5,3.7l-3.6-1.3l1.3-2.7l-8.6-4.7l-10.2,4.7v9.4l-10.5,1.1l-3.9,12.6l-4.6,7l-7,3.2l-1.2,4.7
          l2.8,5.2l-2.1,6.4l-5.4-2.3l-2.4-6.3l-9.2-1.1l3.1,9.2l-1.1,3.7l-7.6,0.8l-6.4,4l-1.8,9.8l3.2,9.5h3.8l-0.1,5.3l4.8-1.8l-0.3,9.4
          l-5,1.9l-5.5,10.9l-4.9,15.3l-7.9,11.6l-2.2,8.3l3,0.5l-2.2,7.4l-3.8,7.2l-3.6-3l-6.8-0.8l-8.3,6.9l-6.7,3.2l0.3,5l-1.5,0.2
          l-0.6,11.7l1.1,3.1l-3.1,0.4l-6,6.6l0.5,4.6l-5.3,10.4l-2.1,8.7l1.8,3.5l4.8-1.9l-3.8,7.6l-4.1,11.9l-7.8,11.4l-6.7,2.7l-2.1,13.4
          l5.3,1.7l-1.1,3.5l2.4,3.3l2.7-1.5l-2.3,12l-10.5,10.9l1.9,5.4l-4.3,10.1l-5.6,3.2l2.5,6l4.8-2.2l11.8,3.1l5.8,8.4l3.1,12.3l6.5,8.9
          l9,4.2l8-7.2l9.8-0.6l5.5,6l1.6,6.6l2.7,4.8l6.4,0.6l17.9-8.2l25.1-3.5l7.7-3.1l1.1-8.7l13.1-14l5.9-17.6l4.7-6.4l10.4-5.8l17.3-9.8
          l15.4-27.6l6.9-23.7l20.4-7.6l8.1-6.9l-1.1-6.6l-3.4-3.2l2.8-5.6l5.4-4.4l1.9,0.8l1.1-5l6.6-6.4l6.7-9.6l9.1-6.1l0.3-4.1l4.3,2.4
          l2.4-2.5l-1.2-2.4l-5.9-1.5l0.2-9.3l4.5-9.8l-6.2-17l9.7-11.4l4.6,0.7l6.5-6.5l3.3,1.8l10.7-5.2l1.1,2l7.4-10.2L735.5,287.9z"/>
        <path id="Khyber_Pakhtunkhwah" :fill="colorme('Khyber Pakhtunkhwa')" stroke="#f8f9fa" d="M652,25.7L637.7,27l-10.6-0.8l-5.9,2l-2.9-0.8l-2.2,1.6l-14.3-0.2l-7.1,4.1L582,34.3l-2.3,3.5l0.9,1.6l-5.6,1l-0.3,2.9l-8,2.1
          l-1.4,3.2h-3.8l-0.7,3.6L563,53l-0.9,2.6l-9.8-5.7L548,56l-0.1,2.9l-15.7,11.7l-2.2,5l8.7,4.7l4.6,6.8l0.6,4.2l3.3,2.4l-2.3,5.4
          l5.6,3.1l-0.9,4.3l2.7,2.6l-4.7,9l6,5.8l-6.9,6.1l0.9,4l-2.7,3.2l-9.4,5.1l-4.7,7.4l-5.2,2.1l-1.4,6.9l-4.1,1.4l0.1,6.1l3.6,3.7
          l4.6,1.9L526,178l0.2,5.3l-3,6.4l-14.9,5.6l-18.8,0.1l-7.7-1.2l-11.3-4.3l-5.7,1.2l-1.9,5l7.3,11.9l5.9,0.7l3.3,4.7l-0.8,6.6
          l5.7,5.4l1.9,5.2l-8.5,6.9l-4.4,0.4L471,242l-7.3,2.7l-4.5-1.8l-3.2,1.9l-7.1-0.2l-3.6,3.9l-0.8,5l2.1,4.3l-3.5,1.2l-3.6,4.9
          l2.9,5.7l-3.2,5.5l-5,2l-2.4,5.1l2.4,5.5l-0.4,13.8l2.3,9.6l10.9,0.5l5.3-5.8l8.4-2.3l-1.5,4.8l3.6,2.3l-1.9,4.1l1.5,1.6l3.8-2.6
          l-1.2,21.9l4.3,2.6l1.3,8.4l2.8-4.9l8.3-4l0.7,8.5l-2,12.4l1.2,2.5l1.5-0.2l-0.3-5l6.7-3.2l8.3-6.9l6.8,0.8l3.6,3l3.8-7.2l2.2-7.4
          l-3-0.5l2.2-8.3l7.9-11.6l4.9-15.3l5.5-10.9l5-1.9l0.3-9.4l-4.8,1.8l0.1-5.3h-3.8l-3.2-9.5l1.8-9.8l6.4-4l7.6-0.8l1.1-3.7l-3.1-9.2
          l9.2,1.1l2.4,6.3l5.4,2.3l2.1-6.4l-2.8-5.2l1.2-4.7l7-3.2l4.6-7l3.9-12.6l10.5-1.1v-9.4l10.2-4.7l8.6,4.7l-1.3,2.7l3.6,1.3l3.5-3.7
          l4.3,2.9l1.3,4.5l-2.6,2.4l5.4,2.1l12.8-4.6l8.3-4.6l2.3-4.7l6.6-3l-5.7-22.3l1.8-5.4l1.5-4.5l8.3,0.5l4.5-11.7l12.7-5.5l5.7-9.3
          l-1.4-2.1l3.3-3.7l-10.6-4.7l-9.3-0.8l-1.5-5.6l0.7-5.7l4.7-5l-26.5-6.5l-8-7l0.3-5.8l-2.4-1.5l-4.9,1.8l-7.6-1.3l-7.7,2.2l-7.9-4.7
          l2.6-6.2l-2.2-3.7l1.3-8.7l15.4-9.2l1.4-4.3l3.7-0.7l5.8-7.8l-1.3-3.9l16.2-4.3l10.7,2.4h13.1l0.3-4.5l-6.4-2.7L652,25.7z"/>
        <path id="Islamabad" :fill="colorme('Islamabad')" stroke="#f8f9fa" d="M609.7,210.7l3.2,6.9l9-4.4l3.4,5.1l-1.9,1.5l3,2.4l5.6-3.6l0.8-4.5l3.9-3.9l-1.6-2.1l-1.4,0.1
          l-5.3-3.9L609.7,210.7z"/>
        <path id="Gilgit_Baltistan" :fill="colorme('Gilgit-Baltistan')" stroke="#f8f9fa" d="M818.7,115.6l-11-12.8l-0.1-6.7l-4.4-4.6l-4-2l-0.4-6.9l-1.6-0.7l-8.5,2.9l-2.4,1.9h-8.1
          l-0.8-5.6l-3.4-4.8l-4.5-0.2l-2.8-2.9l-0.4-3.8l4.1-1.8l-0.9-2.9l2.6-0.3l-3.5-6.7l1.3-6l-4-6.7l-0.6-3.5l-9.4-7.3l-9.2-1.1
          l-0.7,2.5l-3.9,0.1l-3.2-10.9l0.7-1.8l-11.9-2.7l-0.9-1.8l-5.9,0.4l-5.4,4.5l-3.6-3.2l-1.1-4.2l-3.9,2.4l-3.3-4.2l-3.6,0.7l-2,2.8
          l-0.4,4l-2.3-2l-4.9,0.2l-8.3,5.4l-5.1-0.5l-1.2,3.6l-3.7,1.1l-4.5-0.5l-6-3.5l-9.6,0.2l4.2,4.1l6.4,2.7l-0.3,4.5h-13.1l-10.7-2.4
          l-16.2,4.3l1.3,3.9l-5.8,7.8l-3.7,0.7l-1.4,4.3l-15.4,9.2l-1.3,8.7l2.2,3.7l-2.6,6.2l7.9,4.7l7.7-2.2l7.6,1.3l4.9-1.7l2.4,1.4
          l-0.3,5.8l8,7l26.5,6.5l-4.7,5l-0.7,5.7l1.5,5.6l9.3,0.8l10.6,4.7l5.3,2.8l12.3-4.2l4.6,4.9l2,8l16.9,7.6l3.5-3.2l2.8,1.3l2.8-4.3
          l5.1,4.9l1.3,5.7l-2.2,3.4l8.5,5.7l17.7,1.9l15-9.1l4.5,1.8l16.7-8.7l4.4,2.1l6.3-0.3l3.4-9.6l12.1-0.5l0.8-5.5l7.2-1.2L818.7,115.6
          z"/>
        <path id="Azad_Kashmir" :fill="colorme('Azad Kashmir')" stroke="#f8f9fa" d="M726.5,140.9l-2.8,4.3l-2.8-1.3l-3.5,3.2l-16.9-7.6l-2-8l-4.6-4.9l-12.3,4.2l-5.3-2.8
          l-3.3,3.7l1.4,2.1l-5.7,9.3l-12.7,5.5l-4.5,11.7l-8.3-0.5l-1.5,4.5l-1.8,5.4l5.7,22.3l4.3,18l-1.5,4.3l3.1,5.6l-3.1,8.9l3.3,8.9
          l1.3,3.5l-1.6,3.6l8.8,4.9l5.8-1.5l4.5,5l15.4,7.5l6.4-0.2l-1.9-5l-5.1-1.2l1.4-5.7l-7-1.4L670,236l7.9-6.2l0.8-7l-4.9-6.1h-3
          l-3.6-8.4l5.6-5.8l5.1-1.1l4.6-4.9l-2.3-6.5l-16.6-0.7l4.9-10.6l-4.1-7.2l-2.9,1.2l-3.4-0.6l0.2-3.8l6-4.6l-0.1-2.9l2.6-1.6l0.6-7
          h9.5l7.9-6l13.6,1.7l4.6,4l11.6,1l5.8,2.4l10.3-0.4l2.2-3.4l-1.3-5.7L726.5,140.9z"/>
        <path id="Shaksgam_Valley" fill="#b0bec5" stroke="#f8f9fa" d="M769.9,51.7l-1.3,6l3.5,6.7l-2.6,0.3l0.9,2.9l-4.1,1.8l0.4,3.8l2.8,2.9l4.5,0.2l3.4,4.8
          l0.8,5.6h8.1l2.4-1.9l8.5-2.9l1.6,0.7l0.4,6.9l4,2l4.4,4.6L812,96l6.1,4l4.1,0.2l6.5,4l7.4,0.3l3.4,3.2l5-5.2l-2.8-5.9l-5.5-2.2
          l-7.8-0.5l-8.7-6.2l-7.8-2.2l-4.3-2.8l0.8-9.8l-6.7-5.5l-7.1-0.7L769.9,51.7z"/>
        <path id="Ladakh" fill="#b0bec5" stroke="#f8f9fa" d="M928.7,238.7l0.1,3.6l-1.9,3.1l0.6,3.5l4.9,1.7l1,5.3l-1.5,3.5l2.1,2.8l-1.2,6.6l1.1-0.2l-1.6,8.5
          l2,2l8.3-6l3.3-0.3l1.7-4.1l-1.2-4.5l-3.5-3.4l-0.6-3.7l-5.3-6.2l3-11.2L928.7,238.7z"/>
        <path id="Aksai_Chin" fill="#b0bec5" stroke="#f8f9fa" d="M861.5,105.7l2.3,4.3l3.7-2.9l5.9-0.7l1.4,1.6l-4.4,2.8l-1.3,4l3.2,9.2l3.4,3.2l-2.1,2.7
          l8.2,22.2l7.8,3.1l1.6,2.3l5.9-0.7l22,18.1l-4.2,6.9l-10.2,6.2l3.2,3.1l-2.6,3v4.4l3.3,6.9l-3.8,5.8l5.8,10.7l5.9,5.4l0.3-6.6
          l-2.4-5.1l9.3-2.3l-9-18.3l0.4-3.3l4.4-1l6,2l6.8-1.5l6,0.9l6.6-7.9l3.6-10.1l-2.9-8.7l8.4,2.4l2.5-1.3l0.1-5.1l6.9-6.1l8.9-1.9
          l6.3-12.9l0.3-9.5l4.1-8.7l0.4-7.1l2.7-4.8l-1.1-4.3l-5.8-3.4l-3.8,7.1l-4.3,1.3l-5.4-10.6l-3.7,0.8l-3.5-4.1l-5.1-1.2l-2.3-6.8
          l-5.3-5.3l-3.8,0.4l-1.5-6.1l-6.4-0.2l-2.8,3.1l-22.1-0.7L878,97.8l-1.8,5.1l-6.8-1.9l-2.4,1.7l-0.3,3L861.5,105.7z"/>
        <path id="Jammu_Kashmir" fill="#b0bec5" stroke="#f8f9fa" d="M667.4,152.2l-0.6,7l-2.6,1.6l0.1,2.9l-6,4.6l-0.2,3.8l3.4,0.6l2.9-1.2l4.1,7.2l-4.9,10.6
          l16.6,0.7l2.3,6.5l-4.6,4.9l-5.1,1.1l-5.6,5.8l3.6,8.4h3l4.9,6.1l-0.8,7L670,236l9.7,11.2l7,1.4l-1.4,5.7l5.1,1.2l1.9,5l4.2,4.6
          l8.3-5.7l-2.4,7l-0.8,7.2l3.2,6.2l6-0.6l4,1.4l3.7,1.4l3.9-2.6l3.9,4.1l3-0.2l6.2,4.6h8.5l-0.7,3.7l1.4,0.6l4.3-5.5l9.7-5.3l6.5-7.7
          l-0.6-11.5l-5.5-7.5l4.3-0.9l4.2,2.6l7.8-7l8.1-3.4l0.9-3.2l6.2-3.2l15.5,0.6l2.2-1.6l12.6,13.2l17.4,7.6l17.4-9.3l9.9,13.1
          l-0.1,4.5l6,6.4l3.5-3.9l5.8-0.6l7.5-5.2l0.1,6.5l-4.5,9.6l1.8,1.2l4.2-4.4l6.3-5.1l4.8-0.1l5.7-4.9l1.5,11.8l10.1,8.5l4.5-2.4
          l1.4,1l1.1-4.8l7-4.2l1.6-8.5l-1.1,0.2l1.2-6.6l-2.1-2.8l1.5-3.5l-1-5.3l-4.9-1.7l-0.6-3.5l1.9-3.1l-0.1-3.6l-5.5-2.1l-0.1-3.2
          l-6.6-6.1l-5.9-5.4l-5.8-10.7l3.8-5.8l-3.3-6.9v-4.4l2.6-3l-3.2-3.1l10.2-6.2l4.2-6.9l-22-18.1l-5.9,0.7l-1.6-2.3l-7.8-3.1
          l-8.2-22.2l2.1-2.7l-3.4-3.2l-3.2-9.2l1.3-4l4.4-2.8l-1.4-1.6l-5.9,0.7l-3.7,2.9l-2.3-4.3l-34.2,25.8l-7.2,1.2l-0.8,5.5l-12.1,0.5
          l-3.4,9.6l-6.3,0.3l-4.4-2.1l-16.7,8.7l-4.5-1.8l-15,9.1l-17.7-1.9l-8.5-5.7l-10.3,0.4l-5.8-2.4l-11.6-1l-4.6-4l-13.6-1.7l-7.9,6
          L667.4,152.2z"/>
        <path id="Siachin" fill="#b0bec5" stroke="#f8f9fa" d="M807.6,96.1l0.1,6.7l11,12.8l8.6,15.9l34.2-25.8l-22,2l-3.4-3.2l-7.4-0.3l-6.5-4l-4.1-0.2l-6.1-4
          L807.6,96.1z"/>
          <!-- <linearGradient id="SVGID_1_" gradientUnits="userSpaceOnUse" x1="610.3375" y1="708.6" x2="930.3375" y2="708.6">
          <stop  offset="0" style="stop-color:#FFAF7B"/>
          <stop  offset="0.5" style="stop-color:#D76D77"/>
          <stop  offset="1" style="stop-color:#3A1C71"/>
        </linearGradient>
        <rect x="610.3" y="700.6" class="st1" width="320" height="16"/>
        <text transform="matrix(1 0 0 1 607.2591 734.3337)" class="st2 st3">0</text>
        <text transform="matrix(1 0 0 1 764.1816 734.333)" class="st2 st3">50</text>
        <text transform="matrix(1 0 0 1 921.1045 734.3334)" class="st2 st3">100</text> -->
        </svg>
      </div>
      <div class="col-md-6">
        <div class="card card-body border-0 shadow-sm">
          <h6 class="card-title">Cases by Province and Status</h6>
          <Plotly :data="provinces.data" :layout="provinces.layout" :options="provinces.options"></Plotly>
        </div>
      </div>
    </div>
    <!-- END SECOND ROW -->

    <!-- THIRD ROW -->
    <div class="row">
      <div class="col-sm-6 col-md-3">
        <div class="card card-body border-0 shadow-sm mb-4">
          <h6 class="card-title">Cases by Gender</h6>
          <Plotly :data="gender.data" :layout="gender.layout" :options="gender.options"></Plotly>
        </div>
      </div>
      <div class="col-sm-6 col-md-3">
        <div class="card card-body border-0 shadow-sm mb-4">
          <h6 class="card-title">Cases by Source</h6>
          <Plotly :data="source.data" :layout="source.layout" :options="source.options"></Plotly>
        </div>
      </div>
      <div class="col-md-6">
        <div class="card card-body border-0 shadow-sm mb-4">
          <h6 class="card-title">Cases by Age and Gender</h6>
          <Plotly :data="age.data" :layout="age.layout" :options="age.options"></Plotly>
        </div>
      </div>
    </div>
    <!-- END THIRD ROW -->
  </div>
</template>

<script>
import { Plotly } from 'vue-plotly'
import Axios from 'axios'
import moment from 'moment'
export default {
  name: 'App',
  components: { Plotly },
  data () {
    return {
      message: 'Hello Vue!', 
      gradients: [
        '#FFAF7B',
        '#F39B7A',
        '#EA8C79',
        '#E48278',
        '#E07C78',
        '#D76D77',
        '#A95575',
        '#854274',
        '#5B2D72',
        '#4B2572',
        '#3A1C71',
      ],
      data: null,
      statuses: null,
      abc: {},
      ages: {},
      provinces: {
        data: [
          {
            x: [],
            y: [],
            name: 'Admitted, Serious',
            type: 'bar',
            hoverinfo: 'none',
            marker: { color: "#FFAF7B" }
          },
          {
            x: [],
            y: [],
            name: 'Admitted, Stable',
            type: 'bar',
            marker: { color: "#E48278" }
          },
          {
            x: [],
            y: [],
            name: 'Expired',
            type: 'bar',
            marker: { color: "#854274" }
          },
          {
            x: [],
            y: [],
            name: 'Recovered, Discharged',
            type: 'bar',
            marker: { color: "#3A1C71" }
          }
        ],
        layout: {
          autosize: true, 
          barmode: 'stack',
          margin: {
            r: 80,
            b: 100,
            l: 0,
            t: 0,
          },
        },
        options: {
          displayModeBar: false,
          responsive: true
        }
      },
      gender: {
        data: [
          {
            values: [16, 15],
            labels: ['Male', 'Female'],
            hoverinfo: 'label+percent+name',
            hole: .4,
            type: 'pie',
            marker: {
              colors: ['#D76D77', '#3A1C71']
            },
          }
        ],
        layout: {
          legend: {
            x: 1,
            xanchor: 'right',
            y: 1
          },
          margin: {
            r: 0,
            b: 0,
            l: 0,
            t: 0,
          },
        },
        options: {
          displayModeBar: false,
          responsive: true
        }
      },
      source: {
        data: [
          {
            values: [16, 15],
            labels: ['International Travel', 'Human Transmissions'],
            hoverinfo: 'label+percent+name',
            hole: .4,
            type: 'pie',
            marker: {
              colors: ['#D76D77', '#3A1C71']
            },
          }
        ],
        layout: {
          legend: {
            x: 1,
            xanchor: 'right',
            y: 1
          },
          margin: {
            r: 0,
            b: 0,
            l: 0,
            t: 0,
          },
        },
        options: {
          displayModeBar: false,
          responsive: true
        }
      },
      age: {
        data: [
          {
            x: [],
            base: [],
            y: ['0-10', '11-20', '21-30','31-40','41-50','51-60','61-70', '70+'],
            name: 'Male',
            orientation: 'h',
            type: 'bar',
            marker: { color: "#D76D77" }
          },
          {
            x: [],
            y: ['0-10', '11-20', '21-30','31-40','41-50','51-60','61-70', '70+'],
            name: 'Female',
            orientation: 'h',
            type: 'bar',
            marker: { color: "#3A1C71" }
          }
        ],
        layout: {
          autosize: true,
          barmode: 'stack',
          margin: { r: 0, b: 0, l: 50, t: 0 },
        },
        options: {
          displayModeBar: false,
          responsive: true
        }
      }
    }
  },
  computed: {
    admitted () {
      if (this.data) {
        var count = 0
        this.data['Status'].reduce( function(acc, cur) {
          if ((cur == 'Admitted, Stable') || (cur == 'Admitted, Serious'))
            count++
        })
        return count
      }
      return 0
    },
    discharged () {
      if (this.data) {
        var count = 0
        this.data['Status'].reduce( function(acc, cur) {
          if (cur == 'Recovered, Discharged')
            count++
        })
        return count
      }
      return 0
    },
    expired () {
      if (this.data) {
        var count = 0
        this.data['Status'].reduce( function(acc, cur) {
          if (cur == 'Expired')
            count++
        })
        return count
      }
      return 0
    },
    today() {
      return moment().format("Do MMMM YYYY")
    }
  },
  mounted () {
    Axios.all([
      Axios.get('/cases/'),
      Axios.get('/statuses/'),
      Axios.get('/map/'),
      Axios.get('/ages/')
    ]).then( Axios.spread( function(cases, statuses, map, ages) {
      this.data = JSON.parse(cases.data)
      this.statuses = JSON.parse(statuses.data)

      for (let [key, value] of Object.entries(this.data)) {
        this.data[key] = Object.values(this.data[key])
        console.log(value)
      }

      var males = 0
      this.data['Gender'].reduce( function(acc, cur) {
        if (cur == 'Male')
          males++
      })

      var females = 0
      this.data['Gender'].reduce( function(acc, cur) {
        if (cur == 'Female')
          females++
      })

      this.gender.data[0].values = [males, females]

      var travel = 0
      this.data['Source'].reduce( function(acc, cur) {
        if (cur == 'International Travel')
          travel++
      })

      var transmission = 0
      this.data['Source'].reduce( function(acc, cur) {
        if (cur == 'Human Transmission')
          transmission++
      })

      this.source.data[0].values = [travel, transmission]

      var index = 0;
      for (let [key, value] of Object.entries(this.statuses)) {
        this.provinces.data[index].x = []
        this.provinces.data[index].y = []
        for (let [x, y] of Object.entries(value)) {
          console.log(key, value)
          this.provinces.data[index].x.push(x)
          this.provinces.data[index].y.push(y)
          this.provinces.data[index].text = this.provinces.data[index].x.map(String)
        }
        index++
      }

      var counts = map.data
      // counts = this.normalize(counts, 100)
      this.provinces.data[0].x.forEach(function(value, index) {
        this.abc[value] = counts[index]
      }.bind(this));

      this.ages = JSON.parse(ages.data)

      this.age.data[0].x = Object.values(this.ages['Male'])
      this.age.data[0].x.forEach(e => {
        this.age.data[0].base.push(-e)
      })
      this.age.data[1].x = Object.values(this.ages['Female'])

      this.age.data[0].y = Object.keys(this.ages['Male'])
      this.age.data[1].y = Object.keys(this.ages['Female'])
      // console.log(this.ages)
      // for (let [key, value] of Object.entries(this.ages['Male'])) {
      //   console.log(key, value)
      // }

    }.bind(this)))
    .catch (error => console.log(error) )
  },
  methods: {
    colorme(province) {
      if (this.data) {
        var total = this.data['Province'].length
        var value = (this.abc[province] / total) * 100
        this.abc[province] = Math.ceil(value / 10) * 10

        if (this.abc[province] == 10) return '#FFAF7B'
        else if (this.abc[province] == 20) return '#F39B7A'
        else if (this.abc[province] == 30) return '#EA8C79'
        else if (this.abc[province] == 40) return '#E48278'
        else if (this.abc[province] == 50) return '#E07C78'
        else if (this.abc[province] == 60) return '#D76D77'
        else if (this.abc[province] == 70) return '#A95575'
        else if (this.abc[province] == 80) return '#854274'
        else if (this.abc[province] == 90) return '#5B2D72'
        else if (this.abc[province] == 100) return '#4B2572'
        else return '#3A1C71'
      }
    }
  }
}
</script>

