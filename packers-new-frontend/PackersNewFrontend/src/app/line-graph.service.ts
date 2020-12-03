import { Injectable } from '@angular/core';

import { DataPoint } from 'src/app/lineGraphInterface';

@Injectable({
  providedIn: 'root'
})
export class LineGraphService {

  constructor() { }

  formatLineGraphCounts(dates: string[], counts: number[]): DataPoint[] {
    return this.formatLineGraphSeriesCounts(dates, counts);
  }

  formatLineGraphCountsAvg(dates: string[], counts: number[]): DataPoint[] {
    var series = this.formatLineGraphSeriesCounts(dates, counts);
    return this.formatLineGraphTrailingAvg(series, 6);
  }

  /* formats the date to look nice on the xaxis of the graph */
  xAxisFormatMonth(date) {
    return (date.getMonth() + 1) + "/" + date.getDate()  + "/" + date.getFullYear()
  }

  /*******************************************************

    FUNCTION: formatLineGraphSeriesCounts(): DataPoint[]
  
    Creates a chronological series of points of form (date, count).
    Currently creates a data point every week.

  *******************************************************/
  private formatLineGraphSeriesCounts(dates: string[], counts: number[]): DataPoint[] {
    if(dates.length != counts.length) {
      console.error("Data not properly formatted in function formatLineGraphData");
      return null;
    }

    var length = dates.length;
    var series: DataPoint[] = new Array();

    for(var i = 0; i<length; i++) {
      var d: DataPoint;
      var dt = new Date(dates[i])
      
      /* create a new point */
      d = {
        name: dt,
        value: counts[i]
      }
      series.push(d);
    }
    
    /* sort in chronological order */
    series.sort((a, b) => a.name < b.name ? -1 : 1)

    /* create a point every week */
    series = this.fillPeriodicData(series, 7);

    return series;
  }

    /*******************************************************

    FUNCTION: formatLineGraphTrailingAvg(): DataPoint[]
  
    Creates a chronological series of points of form (date, count),
    and takes a trailing average of length trail_length.
    This creates a smoother looking graph

    Currently creates a data point every week.

  *******************************************************/

  private formatLineGraphTrailingAvg(series: DataPoint[], trail_length: number): DataPoint[] {
    var length = series.length;
    var new_series: DataPoint[] = new Array();

    var cur_avg = 0;
    for(var i = 0; i<length; i++) {
      var d: DataPoint;
      
      /* calculate current average */
      if( i < trail_length) {
        cur_avg *= i;
        cur_avg += series[i].value;
        cur_avg /= i+1;
      }
      else {
        cur_avg *= trail_length;
        cur_avg -= series[i-trail_length].value;
        cur_avg += series[i].value;
        cur_avg /= trail_length;
      }

      /* create point */
      d = {
        name: series[i].name,
        value: cur_avg
      }
      new_series.push(d);
    }
    return new_series;
  }

    /*******************************************************

    FUNCTION: fillPeriodicData(): DataPoint[]
  
    Takes a series and creates a datapoint at every num_days, 
    where the count is the sum of counts of all days in between points.

  *******************************************************/

  private fillPeriodicData(series: DataPoint[], num_days: number): DataPoint[] {
    var length = series.length;
    var periodicSeries: DataPoint[] = new Array();
    var startingDate: Date = new Date(series[0].name);

    var i = 0;
    while(i < length) {
      var nextPeriod: Date = new Date(startingDate);
      nextPeriod.setDate(nextPeriod.getDate() + num_days);

      /* grab all data points in between dates */
      var periodCount = 0;
      while(i < length && series[i].name < nextPeriod) {
        periodCount+=series[i].value;
        i+=1;
      }

      /* create and push new point */
      periodicSeries.push({
        name: startingDate,
        value: periodCount
      });

      /* move our starting date to next point */
      startingDate = nextPeriod;
    }

    return periodicSeries;

  }
}
