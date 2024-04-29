function createCircle(radius) {  
return {
    radius,
    draw() {
        console.log('draw2');
    }
};
}
//Factory functions

const circle1 = createCircle(14);
console.log(circle1);

const circle2 = createCircle(4);
console.log(circle2);
