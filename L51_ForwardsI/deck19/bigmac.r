library(data.table)
library(ggplot2)

X<-data.table(read.csv("source.csv",stringsAsFactors=FALSE))
X[,date:=as.Date(date)]
X<-subset(X,is.element(iso_a3,c("MEX","USA")))
X[,dollar_price:=local_price/dollar_ex]
setnames(X,"name","Country")
p<-ggplot(data=X)
p<-p+geom_line(aes(group=factor(Country),x=date,y=dollar_price,colour=Country),size=1)
p<-p+theme_minimal()
p<-p+labs(title="Big Mac Index",x="Year",y="Price in USD")
ggsave("bigmac.pdf",height=3,width=5)

