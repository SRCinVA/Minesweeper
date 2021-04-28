int sinVal;
int cosVal;
int j;

void setup() {

Serial.begin(9600);
}

void loop() {
    for(j=0,j<=2*3.14159265;j=j+.01){ //notice the tiny increment; this is to help create a smooth curve.
        sinVal=sin(j);
        cosVal=cos(j);
        Serial.print(sinVal);
        Serial.print(",");     // a delimiter, just to make it easier to read.

    }
}