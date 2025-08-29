
!pip install reportlab seaborn matplotlib pandas

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4


df = pd.read_csv("HR_Analytics.csv")   # <- dataset file upload 


# Pie Chart: Attrition
plt.figure(figsize=(5,5))
df['Attrition'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=["#66b3ff","#ff9999"])
plt.title("Attrition Distribution")
plt.ylabel("")
plt.savefig("attrition_pie.png")
plt.close()

# Bar Chart: BusinessTravel
plt.figure(figsize=(6,4))
df['BusinessTravel'].value_counts().plot(kind='bar', color=["#008080","#FF6347","#4682B4"])
plt.title("Business Travel Frequency")
plt.xlabel("Travel Type")
plt.ylabel("Count")
plt.savefig("business_travel_bar.png")
plt.close()

# Correlation Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.close()


doc = SimpleDocTemplate("Final_Assignment_Report.pdf", pagesize=A4)
styles = getSampleStyleSheet()
story = []

story.append(Image("WhatsApp Image 2025-08-26 at 18.01.15_7dda6489.jpg", width=400, height=500))
story.append(PageBreak())

# Report Title
story.append(Paragraph("<b>Dataset Analysis Report</b>", styles['Title']))
story.append(Spacer(1, 20))

# Project Title
story.append(Paragraph("<b>Project Title:</b> Employee Attrition and Factors Analysis", styles['Normal']))
story.append(Spacer(1, 12))

# Types of Data
story.append(Paragraph("<b>1. Types of Data:</b>", styles['Heading2']))
story.append(Paragraph("• Numerical (Continuous): Age, DailyRate, MonthlyIncome, YearsAtCompany", styles['Normal']))
story.append(Paragraph("• Categorical (Nominal): Attrition, BusinessTravel, Department, Gender", styles['Normal']))
story.append(Paragraph("• Ordinal: Education, JobLevel", styles['Normal']))
story.append(Spacer(1, 12))

# Balanced vs Imbalanced
attrition_counts = df['Attrition'].value_counts()
attrition_perc = df['Attrition'].value_counts(normalize=True)*100
story.append(Paragraph("<b>2. Balanced vs Imbalanced Dataset:</b>", styles['Heading2']))
story.append(Paragraph(f"Attrition Counts: {dict(attrition_counts)}", styles['Normal']))
story.append(Paragraph(f"Attrition Percentage: {dict(attrition_perc.round(2))}", styles['Normal']))
story.append(Image("attrition_pie.png", width=250, height=250))
story.append(Spacer(1, 12))

# Statistical Analysis
story.append(Paragraph("<b>3. Statistical Analysis:</b>", styles['Heading2']))
story.append(Paragraph(f"Age → Mean: {df['Age'].mean():.2f}, Median: {df['Age'].median()}, "
                       f"Variance: {df['Age'].var():.2f}, Std Dev: {df['Age'].std():.2f}", styles['Normal']))
story.append(Paragraph(f"BusinessTravel Frequency: {dict(df['BusinessTravel'].value_counts())}", styles['Normal']))
story.append(Image("business_travel_bar.png", width=350, height=250))
story.append(Spacer(1, 12))

# Correlation Heatmap
story.append(Paragraph("<b>4. Correlation Heatmap:</b>", styles['Heading2']))
story.append(Image("heatmap.png", width=400, height=300))
story.append(Spacer(1, 12))

# Missing Values
story.append(Paragraph("<b>5. Missing Values:</b>", styles['Heading2']))
missing = df.isnull().sum().to_dict()
story.append(Paragraph(f"Missing values per column: {missing}", styles['Normal']))
story.append(Spacer(1, 12))

# Encoding
story.append(Paragraph("<b>6. Categorical to Numerical Conversion:</b>", styles['Heading2']))
story.append(Paragraph("Categorical data like Attrition can be converted using Label Encoding (Yes=1, No=0). "
                       "Department, JobRole ইত্যাদি One-Hot Encoding এর মাধ্যমে numerical এ রূপান্তর করা যাবে।", styles['Normal']))
story.append(Spacer(1, 12))

# Conclusion
story.append(Paragraph("<b>7. Conclusion:</b>", styles['Heading2']))
story.append(Paragraph("Dataset", styles['Normal']))


doc.build(story)

print("✅ Final Report Generated: Final_Assignment_Report.pdf")