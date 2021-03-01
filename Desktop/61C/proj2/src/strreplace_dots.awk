#String replacement awk script

BEGIN{
  
}

/t7/{
#rst
  gsub("t7","t1");
}

/t8/{
#rst
  gsub("t8","t2");
}

/t9/{
#rst
  gsub("t9","t3");
}

/t10/{
#rst
  gsub("t10","t4");
}

#MAIN
{
  print $0;
}
END{
  
}

