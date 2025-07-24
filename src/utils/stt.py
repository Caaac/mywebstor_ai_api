from abc import ABC, abstractmethod

class AbstractModel(ABC):
  @abstractmethod
  def transcript():
    raise NotImplementedError
  
class STTModel(AbstractModel):
  ...