// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var ctx = document.getElementById("masSolicitadosPie");
const masSolicitadosPieElement = document.getElementById('mas_solicitados');
const textContentPie = masSolicitadosPieElement.textContent;
const dataPie = eval(textContentPie);
const labelsChartPie = data.map(producto => producto.Nombre_Producto);
const dataChartPie = data.map(producto => producto.Cantidad);

var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: labelsChartPie,
    datasets: [{
      data: dataChartPie,
      backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc','#ffa1b3','#90ee90','#f0e68c','#add8e6','#d7ccc8','#e0627c','#f9d28b'],
      hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf','#ff7096','#64dd17','#d6ce6c','#87ceeb','#b0a9a5','#c14661','#f5b75e'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});
