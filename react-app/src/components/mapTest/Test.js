import React from 'react'
import { GoogleMap, LoadScript } from '@react-google-maps/api';

const containerStyle = {
  width: '400px',
  height: '400px'
};

const center = {
  lat: -3.745,
  lng: -38.523
};

function Test() {
  return (
    <LoadScript
      googleMapsApiKey="AIzaSyCYIobr1Us9oXVAuMYRjMlo7OtR16PstsM"
    >
      <GoogleMap
        mapContainerStyle={containerStyle}
        center={center}
        zoom={10}
      >
        {  }
        <></>
      </GoogleMap>
    </LoadScript>
  )
}

export default React.memo(Test)