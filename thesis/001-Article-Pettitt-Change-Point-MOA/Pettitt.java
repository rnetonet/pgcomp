package moa.classifiers.core.driftdetection;

import com.github.javacliparser.FloatOption;
import com.github.javacliparser.IntOption;
import moa.core.ObjectRepository;
import moa.tasks.TaskMonitor;

import java.util.*;

/**
    * Drift detection method based in Pettitt
    *
    *
    * @author Ruivaldo Neto (rneto@rneto.net)
    * @version $Revision: 7 $
    */
public class Pettitt extends AbstractChangeDetector {

    private static final long serialVersionUID = 5210470661274384763L;

    public IntOption minNumInstancesOption = new IntOption(
            "minNumInstances",
            'n',
            "The minimum number of instances before permitting detecting change.",
            100, 0, Integer.MAX_VALUE);


    private ArrayList<Double> dataList;
    private Integer changePoint;
    private Integer nDataWhenChangePoint;

    public Pettitt() {
        resetLearning();
    }

    @Override
    public void resetLearning() {
        this.dataList = new ArrayList<Double>();

        this.changePoint = null;
        this.nDataWhenChangePoint = null;

        this.isChangeDetected = false;
        this.isInitialized = false;
    }

    @Override
    public void input(double inputData) {
        if (this.isChangeDetected) {
            this.isChangeDetected = false;
            dataList.add(inputData);
            return;
        }

        dataList.add(inputData);

        int dataS = dataList.size();

        int[] vecSize = new int[dataS];
        for (int i = 1; i <= dataS; i++) {
            vecSize[i - 1] = i;
        }

        Double[] data = new Double[dataS];
        dataList.toArray(data);

        int[] dataRank = rank(data);

        int[] dataRankSum = new int[dataS];
        dataRankSum[0] = dataRank[0];
        for (int i = 1; i < dataRank.length; i++) {
            dataRankSum[i] = dataRank[i] + dataRankSum[i - 1];
        }

        int[] sumData = new int[dataS];
        for (int i = 1; i < sumData.length; i++) {
            sumData[i] = (2 * dataRankSum[i]) - (i * (dataS + 1));
        }

        int[] absSumData = new int[dataS];
        for (int i = 0; i < absSumData.length; i++) {
            absSumData[i] = Math.abs(sumData[i]);
        }

        Integer maxAbsSumData = Arrays.stream(absSumData).max().getAsInt();

        // Find Index
        int newChangePoint = 0;
        for (newChangePoint = 0; newChangePoint < absSumData.length; newChangePoint++) {
            if (absSumData[newChangePoint] == maxAbsSumData) {
                break;
            }
        }

        // First Index
        if (this.changePoint == null) {
            this.changePoint = newChangePoint;
            this.nDataWhenChangePoint = this.dataList.size();
            return;
        }

        // If different, concept drift
        int changePointDelta = newChangePoint - this.changePoint;
        int nDataDelta = dataList.size() - this.nDataWhenChangePoint;

        if (changePointDelta >= this.minNumInstancesOption.getValue() && changePointDelta >= nDataDelta / 2 + 1) {
            this.changePoint = newChangePoint;
            this.nDataWhenChangePoint = this.dataList.size();

            this.isChangeDetected = true;

            return;
        }
    }

    private static int[] rank(Double[] x){
        int [] R = new int[x.length];
        if(x.length == 0)return R;
        Integer [] I = new Integer[x.length];
        for(int i = 0; i < x.length; i++) {
            I[i] = i;
        }
        Arrays.sort(I, (i0, i1) -> (int) Math.signum(x[i0]-x[i1]));
        int j = 0;
        for(int i = 0; i < x.length; i++){
            if(x[I[i]] != x[I[j]])
                j = i;
            R[I[i]] = j;
        }
        return R;
    }

    @Override
    public void getDescription(StringBuilder sb, int indent) {
        // TODO Auto-generated method stub
    }

    @Override
    protected void prepareForUseImpl(TaskMonitor monitor,
                                        ObjectRepository repository) {
        // TODO Auto-generated method stub
    }
}