# Database Schema

## Table: signals

Every collected article, publication, conference abstract, press release, regulatory update, or announcement is converted into a signal.

### Primary Fields

- signal_id
- signal_date

### Source Information

- source
- source_category
- source_url

### Classification

- topic
- subtopic

### Organizations

- company
- partner_company
- competitor
- pharma_adopter

### Scientific Attributes

- modality
- target
- technology
- platform
- product
- indication

### Business Attributes

- event_type
- deal_type

### Manufacturing Attributes

- manufacturing_area
- capability

### Regulatory Attributes

- regulatory_body
- validation_stage

### Intelligence Attributes

- impact_score
- confidence_level
- strategic_relevance

### Evidence

- title
- summary
- raw_text
- url

### Audit Fields

- date_collected
- date_processed
