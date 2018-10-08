concept.drift<-function(x, plot=T){
    dataS <- length(x)
    vecSize <- 1:dataS
    dataRank <- rank(x)
    sumData <- sapply(vecSize, 
        function(x) 2 * sum(dataRank[1:x]) - x * (dataS + 1))
    absSumData <- abs(sumData)
    maxAbsSumData <- max(absSumData)
    change.point<-vecSize[maxAbsSumData == absSumData]
    if(plot){
        plot(x, t="l", main=paste("Concept Drift:", change.point))
        abline(v=change.point, col="red")
    }
    change.point
}  