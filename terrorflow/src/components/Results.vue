<template>

<div @click="quitResults" class="imagedrop results-screen animated fadeIn" style="position: relative">

<div class="divvy">
<results-chart :width="480" :height="300" :options="plotOpts" :pred="predToShow"></results-chart>

</div>

</div>

</template>

<script>
export default {
    props: ['quitResults', 'predToShow'],
    data() {
        return {
            plotOpts: {
                scaleOverride: true,
                scaleStartValue: 0,
                scaleEndValue: 1,
                scale: {
                    ticks: {
                        stepSize: 0.25,
                        max: 1,
                        display: false
                    }
                },
                legend: {
                    display: true,
                    position: 'right',
                },
                tooltips: {
                    backgroundColor: '#aaa',
                    bodyFontFamily: 'Lato',
                    bodyFontSize: 20,
                    paddingBottom: 12
                },
                elements: {
                    arc: {
                        borderWidth: 3,
                        borderColor: '#eee'
                    }
                },
                gridLines: {
                    display: false
                },
                ticks: {
                    display: false
                },
                scales: {
                    ticks: {
                        display: false,
                    },
                    display: false,
                    xAxes: [{
                        display: false
                    }],
                    yAxes: [{
                        display: false,
                        ticks: {
                            min:0,
                            max:0
                        }
                    }],
                },
                scaleShowLabels: false,
            }
        }
    }
}
</script>


<style>

.divvy {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
}

.results-screen {
    background: #eee;
    border: none;
    box-shadow: 1px 1px 6px #333;
    cursor: pointer;
}

</style>