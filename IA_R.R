library(tidyverse)

pakistan2 <- read.csv('C:/Users/Joel/Documents/Individual Assignment/Individual-Assignment/pakistan2.csv')

pakistan2_summarized <- pakistan2 %>%
  group_by(year) %>%
  summarize(mean_Casualty_ratio = mean(Casualty_ratio))
          
eventsp_year = pakistan2 %>%
  group_by(year) %>%
  count(year)

pakistan2_final = merge(pakistan2_summarized, eventsp_year, by = "year")

ggplot(pakistan2_final) +
  geom_bar(mapping=aes(x = year, y = mean_Casualty_ratio, fill = n), stat='identity') +
  labs(title ="Final Bar Plot", x = "Year", y = "Mean casualty ratio (high/low estimate)") +
  scale_fill_gradient(low = "blue", high = "red", name = "Number of events") +
  theme_bw()
  

