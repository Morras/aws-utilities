[budget.template](budget.template) will setup an AWS budget to alert you if any resources are incurring a cost outside your designated AWS region.

The template will monitor for usage outside EU (Ireland) region, but you can change this by altering the Region list filter.

The template takes an email where notifications of a budget breach is sent, and a threshold. Note that CloudFront will incur changes where the data is leaving the AWS network, so if you have large CloudFront charges, you might not be able to use this solutoin without filtering CloudFront out as well.
