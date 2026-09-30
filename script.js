let workouts = [];
let total = 0;
function addWorkout(){
  let w = document.getElementById('workout').value;
  let c = parseInt(document.getElementById('calories').value) || 0;
  if(!w) return alert("Workout enter pannu da!");
  workouts.push({w, c});
  total += c;
  document.getElementById('count').innerText = workouts.length;
  document.getElementById('totalCal').innerText = total;
  let li = document.createElement('li');
  li.innerText = `${w} - ${c} cal`;
  document.getElementById('list').appendChild(li);
  document.getElementById('workout').value = '';
  document.getElementById('calories').value = '';
}
