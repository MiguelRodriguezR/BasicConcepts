package com.notjet.calc;

import android.graphics.Color;
import android.graphics.DashPathEffect;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import com.androidplot.util.PixelUtils;
import com.androidplot.xy.CatmullRomInterpolator;
import com.androidplot.xy.LineAndPointFormatter;
import com.androidplot.xy.PanZoom;
import com.androidplot.xy.SimpleXYSeries;
import com.androidplot.xy.StepModelFit;
import com.androidplot.xy.XYGraphWidget;
import com.androidplot.xy.XYPlot;
import com.androidplot.xy.XYSeries;

import java.text.DecimalFormat;
import java.text.FieldPosition;
import java.text.Format;
import java.text.ParsePosition;
import java.util.Arrays;

public class Graph2Activity extends AppCompatActivity {

    private static final int NUM_GRIDLINES = 6;

    private XYPlot plot;
    private PanZoom panZoom;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_graph2);

        // initialize our XYPlot reference:
        plot = (XYPlot) findViewById(R.id.plot);

        // set a fixed origin and a "by-value" step mode so that grid lines will
        // move dynamically with the data when the users pans or zooms:
        plot.setUserDomainOrigin(0);
        plot.setUserRangeOrigin(0);

        // predefine the stepping of both axis
        // increment will be chosen from list to best fit NUM_GRIDLINES grid lines
        double[] inc_domain = new double[]{0.1,1,5,10,50,100,500};
        double[] inc_range = new double[]{0.1,1,5,10,20,50,100};
        plot.setDomainStepModel(new StepModelFit(plot.getBounds().getxRegion(),inc_domain,NUM_GRIDLINES));
        plot.setRangeStepModel( new StepModelFit(plot.getBounds().getyRegion(),inc_range,NUM_GRIDLINES));


        panZoom = PanZoom.attach(plot);

        // create a couple arrays of y-values to plot:
        //final Number[] domainLabels = {-1, 2, 3, 6, 7, 8, 9, 10, 13, 14};
        Number[] series1Numbers = {1, 4, 2, 8, 4, 16, 8, 32, 16, 64};
        Number[] series2Numbers = {-5, 2, 10, 5, 20, 10, 40, 20, 80, 40};
        Number[] series3Numbers = {0, 1, 2, 3, 4, 5, 6};

        // turn the above arrays into XYSeries':
        // (Y_VALS_ONLY means use the element index as the x value)
        XYSeries series1 = new SimpleXYSeries(
                Arrays.asList(series1Numbers), SimpleXYSeries.ArrayFormat.Y_VALS_ONLY, "Serie uno");
        XYSeries series2 = new SimpleXYSeries(
                Arrays.asList(series2Numbers), SimpleXYSeries.ArrayFormat.Y_VALS_ONLY, "Serie dos");
        XYSeries series3 = new SimpleXYSeries(
                Arrays.asList(series3Numbers), SimpleXYSeries.ArrayFormat.Y_VALS_ONLY, "linea");

        // create formatters to use for drawing a series using LineAndPointRenderer
        // and configure them from xml:
        LineAndPointFormatter series1Format =
                new LineAndPointFormatter(Color.RED, Color.GREEN, null, null);

        LineAndPointFormatter series2Format =
                new LineAndPointFormatter(Color.BLUE, Color.GRAY, null, null);

        LineAndPointFormatter series3Format =
                new LineAndPointFormatter(Color.GREEN, Color.GRAY, null, null);

        // add an "dash" effect to the series2 line:
        series2Format.getLinePaint().setPathEffect(new DashPathEffect(new float[] {

                // always use DP when specifying pixel sizes, to keep things consistent across devices:
                PixelUtils.dpToPix(20),
                PixelUtils.dpToPix(15)}, 0));

        // just for fun, add some smoothing to the lines:
        // see: http://androidplot.com/smooth-curves-and-androidplot/
        series1Format.setInterpolationParams(
                new CatmullRomInterpolator.Params(10, CatmullRomInterpolator.Type.Centripetal));

        series2Format.setInterpolationParams(
                new CatmullRomInterpolator.Params(10, CatmullRomInterpolator.Type.Centripetal));

        // add a new series' to the xyplot:
        plot.addSeries(series1, series1Format);
        plot.addSeries(series2, series2Format);
        plot.addSeries(series3, series3Format);

       /* plot.getGraph().getLineLabelStyle(XYGraphWidget.Edge.BOTTOM).setFormat(new Format() {
            @Override
            public StringBuffer format(Object obj, StringBuffer toAppendTo, FieldPosition pos) {
                int i = Math.round(((Number) obj).floatValue());
                return toAppendTo.append(domainLabels[i]);
            }
            @Override
            public Object parseObject(String source, ParsePosition pos) {
                return null;
            }
        });*/

        plot.getGraph().getLineLabelStyle(XYGraphWidget.Edge.BOTTOM).
                setFormat(new DecimalFormat("#####.#"));
    }
}
